def check_negative_effects(time_spent_on_social_media: int, num_of_friends: int, 
use_while_studying: bool) -> None:
    if time_spent_on_social_media > 4:
        print("You may be spending too much time on social media.")
    if num_of_friends > 500:
        print("You may have too many friends on social media.")
    if use_while_studying:
        print("Using social media while studying may be affecting your focus.")
# Test the function
check_negative_effects(5, 600, True)
