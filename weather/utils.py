from rest_framework.reverse import reverse

def generate_links(request, location_name=None, user_id=None):
    links = {
        "self": {
            "href": request.build_absolute_uri()
        },
        "weather_data": {
            "href": request.build_absolute_uri(reverse('weather-data-api', args=[location_name])) if location_name else None
        },
        "daily_recommendations": {
            "href": request.build_absolute_uri(reverse('daily-recommendations', args=[location_name])) if location_name else None
        },
        "planned_recommendations": {
            "href": request.build_absolute_uri(reverse('planned-recommendations-api', args=[location_name, 7])) if location_name else None  # Assuming 7 days ahead
        },
        "user_preferences": {
            "href": request.build_absolute_uri(reverse('user-preferences'))
        },
        "update_user_preferences": {
            "href": request.build_absolute_uri(reverse('update-user-preferences', args=[user_id, "field", "value"])) if user_id else None
        },
        "chatbot": {
            "href": request.build_absolute_uri(reverse('chatbot-api', args=["message"]))  # Replace "message" with a dynamic value if needed
        }
    }
    return links