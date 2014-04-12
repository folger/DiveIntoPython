from plural import build_match_and_apply_functions


class LazyRules:
    rules_filename = 'plural_rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index-1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        return funcs


def plural(noun):
    for matches_rule, apply_rule in LazyRules():
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

if __name__ == '__main__':
    print(plural('ass'))
    print(plural('wax'))
    print(plural('orz'))
    print(plural('touch'))
    print(plural('boy'))
    print(plural('Folger'))
    print(plural('Lun'))
