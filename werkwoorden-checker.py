import random

dictionary = {
    "read": {"infinitief": "lezen", "verleden": "las", "voltooid": "gelezen"},
    "see": {"infinitief": "zien", "verleden": "zag", "voltooid": "gezien"},
}
list_of_keys = list(dictionary.keys())
random_translation = random.choice(list_of_keys)
exp_inf = dictionary[random_translation]["infinitief"]
exp_past = dictionary[random_translation]["verleden"]
exp_perf = dictionary[random_translation]["voltooid"]


def check(given_inf: str, given_pas: str, given_perf: str, attempt: int) -> None:
    if not attempt:
        print("Repeat words and try later")
        return
    if given_inf == exp_inf:
        if given_pas == exp_past:
            if given_perf == exp_perf:
                print("Good Job!")
            else:
                given_perf = input("Voltooid is wrong. Try again: ")
                attempt -= 1
                check(given_inf, given_pas, given_perf, attempt)
        else:
            given_pas = input("Verleden is wrong. Try again: ")
            attempt -= 1
            check(given_inf, given_pas, given_perf, attempt)
    else:
        given_inf = input("Infinitief is wrong. Try again: ")
        attempt -= 1
        check(given_inf, given_pas, given_perf, attempt)


answer = input(
    f"Type verb in infinitief, verleden and voltooid time separated by space for '{random_translation}': "
)
list_of_answers = answer.split()
check(list_of_answers[0], list_of_answers[1], list_of_answers[2], 3)
