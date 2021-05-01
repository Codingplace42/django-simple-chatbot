from collections import Counter


class PatternMatcher:
    def __init__(self, tokens, patterns):
        self.tokens = tokens
        self.patterns = patterns

    @staticmethod
    def get_token_match_ratio(input_token_list, sample_token_list):
        matches = [token for token in input_token_list if token in sample_token_list]
        return (len(matches), len(input_token_list))

    def get_pattern_statistics(self):
        statistics = dict()
        for pattern in self.patterns:
            match_ratio = self.get_token_match_ratio(
                input_token_list=self.tokens,
                sample_token_list=pattern.tokenized_string.split()
            )
            abs_ = abs(match_ratio[0] - match_ratio[1])
            if abs_ in statistics:
                statistics[abs_].append(pattern)
            else:
                statistics[abs_] = [pattern]
        return statistics

    def get_best_matched_tag(self):
        # Statistics:
        #   {abs_1: [pattern_11, ..., pattern_1n],
        #    abs_2: [pattern_21, ..., pattern_2n]}
        # Pattern must not be unique in abs

        statistics = self.get_pattern_statistics()
        abs_list = list(statistics.keys())
        min_abs = min(abs_list)
        tags = [pattern.tag for pattern in statistics[min_abs]]
        tag_counter = dict(Counter(tags))
        return max(tag_counter, key=tag_counter.get)
