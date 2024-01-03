import random

dictionary = {
    "read": {"infinitief": "lezen", "verleden": "las", "voltooid": "gelezen"},
    "see": {"infinitief": "zien", "verleden": "zag", "voltooid": "gezien"},
}
list_of_keys = list(dictionary.keys())
random_translation = random.choice(list_of_keys)


answer = input(
    f"Type verb in infinitief, verleden and voltooid time separated by space for {random_translation}: "
)
list_of_answers = answer.split()
if (
    list_of_answers[0] == dictionary[random_translation]["infinitief"]
    and list_of_answers[1] == dictionary[random_translation]["verleden"]
    and list_of_answers[2] == dictionary[random_translation]["voltooid"]
):
    print("Yay!")
else:
    print("Nope")
