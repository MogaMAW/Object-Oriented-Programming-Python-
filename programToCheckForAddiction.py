def social_media_addiction_level(time_spent_on_social_media: int) -> str:
    if time_spent_on_social_media < 2:
        return "Low"
    elif time_spent_on_social_media < 4:
        return "Moderate"
    else:
        return "High"
# Test the function
#to see the possible outcomes 
print(social_media_addiction_level(1)) #  Low 
print(social_media_addiction_level(3)) # Moderate
print(social_media_addiction_level(5)) # High
