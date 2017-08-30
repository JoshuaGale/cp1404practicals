def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv", "r")
    scores_data = scores_file.readlines()
    #print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    subject_scores = group_subject_scores(score_values)
    display_subject_details(subject_scores, subjects)


def group_subject_scores(score_values):
    subject_scores = []
    number_of_subjects = len(score_values[0])
    for score in range(number_of_subjects):
        single_subject_scores = []
        for scores in score_values:
            single_subject_scores.append(scores.pop(0))
        subject_scores.append(single_subject_scores)
    return subject_scores


def display_subject_details(subject_scores, subject_names):
    for i, single_subject_scores in enumerate(subject_scores):
        print(subject_names[i], "Scores:")
        for score in single_subject_scores:
            print("{:>2}".format(score), end=" ")
        print("\nMax: {}".format(max(single_subject_scores)))
        print("Min: {}".format(min(single_subject_scores)))
        print("Avg: {:.1f}\n".format(
            (sum(single_subject_scores) / len(single_subject_scores))))


main()