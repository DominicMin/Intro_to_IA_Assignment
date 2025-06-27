EMPTY_INFO={
    "business_name": None,
    "location": None,
    "opening_hours": None,
    "business_info": None,
    "restaurant_name": None,
    "recommendation_reason": None,
    "facility_name": None,
    "facility_info": None,
    "building_name": None,
    "building_include": None,
    "handbook_info": None,
    "query_topic": None
}



Templates={
    "ask_business_location":{
        "info":["business_name","location"],
        "positive": "Great! {business_name} is located at {location}. You can easily find it there!",
        "neutral": "{business_name} is located at {location}.",
        "negative": "I understand you need to find {business_name}. It's located at {location}.",
        "info_not_found": "I'm sorry, I couldn't find location information for {business_name} at the moment."
    },
    "ask_business_time":{
        "info":["business_name","opening_hours"],
        "positive": "Perfect! {business_name} is open {opening_hours}. Hope you have a great visit!",
        "neutral": "{business_name} operates during {opening_hours}.",
        "negative": "I know it can be frustrating when you need to know the hours. {business_name} is open {opening_hours}.",
        "info_not_found": "I'm sorry, I don't have the operating hours for {business_name} available right now."
    },
    "ask_business_info":{
        "info":["business_name","business_info"],
        "positive": "Excellent choice! Here's what I know about {business_name}: {business_info}",
        "neutral": "Here's information about {business_name}: {business_info}",
        "negative": "I understand you need information about {business_name}. Here's what I can tell you: {business_info}",
        "info_not_found": "I'm sorry, I don't have detailed information about {business_name} available at the moment."
    },
    "ask_restaurant_location":{
        "info":["restaurant_name","location"],
        "positive": "Wonderful! {restaurant_name} is located at {location}. Enjoy your meal!",
        "neutral": "{restaurant_name} can be found at {location}.",
        "negative": "I hope this helps - {restaurant_name} is located at {location}.",
        "info_not_found": "I'm sorry, I couldn't find the location of {restaurant_name} right now."
    },
    "ask_restaurant_time":{
        "info":["restaurant_name","opening_hours"],
        "positive": "Great timing! {restaurant_name} is open {opening_hours}. Have a delicious meal!",
        "neutral": "{restaurant_name} operates during {opening_hours}.",
        "negative": "I understand you're looking for meal times. {restaurant_name} is open {opening_hours}.",
        "info_not_found": "I'm sorry, I don't have the operating hours for {restaurant_name} available."
    },
    "ask_restaurant_recommendation":{
        "info":["restaurant_name","recommendation_reason"],
        "positive": "I'd love to recommend {restaurant_name}! {recommendation_reason}",
        "neutral": "I suggest {restaurant_name}. {recommendation_reason}",
        "negative": "I understand choosing a restaurant can be difficult. I recommend {restaurant_name} because {recommendation_reason}",
        "info_not_found": "I'm sorry, I don't have enough information to make a restaurant recommendation at the moment."
    },

    "ask_facility_location":{
        "info":["facility_name","location"],
        "positive": "Perfect! {facility_name} is located at {location}. Hope it's helpful!",
        "neutral": "{facility_name} is situated at {location}.",
        "negative": "I hope this helps you find what you need - {facility_name} is at {location}.",
        "info_not_found": "I'm sorry, I couldn't locate {facility_name} at the moment."
    },
    "ask_facility_time":{
        "info":["facility_name","opening_hours"],
        "positive": "Excellent! {facility_name} is available {opening_hours}. Enjoy using the facility!",
        "neutral": "{facility_name} operates during {opening_hours}.",
        "negative": "I understand you need to know when it's open. {facility_name} is available {opening_hours}.",
        "info_not_found": "I'm sorry, I don't have the operating hours for {facility_name}."
    },
    "ask_facility_info":{
        "info":["facility_name","facility_info"],
        "positive": "Great! Here's what I know about {facility_name}: {facility_info}",
        "neutral": "Here's information about {facility_name}: {facility_info}",
        "negative": "I understand you need information about {facility_name}. Here's what I can tell you: {facility_info}",
        "info_not_found": "I'm sorry, I don't have detailed information about {facility_name} available at the moment."
    },
    "ask_building_location":{
        "info":["building_name","location"],
        "positive": "Great! {building_name} is located at {location}. Enjoy your stay!",
        "neutral": "{building_name} is situated at {location}.",
        "negative": "I hope this helps you find what you need - {building_name} is at {location}.",
        "info_not_found": "I'm sorry, I couldn't find the location of {building_name} right now."
    },
    "ask_building_include":{
        "info":["building_name","building_include"],
        "positive": "Great question! {building_name} includes: {building_include}",
        "neutral": "{building_name} contains the following: {building_include}",
        "negative": "I understand you need to know what's available. {building_name} includes: {building_include}",
        "info_not_found": "I'm sorry, I don't have information about what's included in {building_name}."
    },
    "ask_handbook_info":{
        "info":["handbook_info"],
        "positive": "Happy to help! Here's the handbook information you need: {handbook_info}",
        "neutral": "According to the handbook: {handbook_info}",
        "negative": "I understand you need guidance. The handbook states: {handbook_info}",
        "info_not_found": "I'm sorry, I couldn't find that information in the handbook at the moment."
    },
    "entity_not_found":{
        "info":["query_topic"],
        "positive": "I'd love to help! Could you please provide more details about {query_topic}?",
        "neutral": "I couldn't identify the specific item you're asking about. Could you clarify {query_topic}?",
        "negative": "I understand this might be frustrating. Could you please rephrase or provide more details about {query_topic}?",
        "info_not_found": "I'm sorry, I couldn't understand what you're looking for. Could you please be more specific?"
    },
    "unknown_intent":{
        "positive": "I'd be happy to help! Could you please rephrase your question so I can better assist you?",
        "neutral": "I'm not sure how to help with that. Could you please clarify what you're looking for?",
        "negative": "I understand this might be confusing. Could you please explain what you need help with?",
        "info_not_found": "I'm sorry, I don't understand your request. Could you please ask in a different way?"
    }
}

def match_template(intent, sentiment, info):
    
    if intent not in Templates:
        # Use unknown_intent template
        template = Templates["unknown_intent"]
        if sentiment in template:
            return template[sentiment]
        else:
            return template["info_not_found"]
    
    template = Templates[intent]
    
    # Get the required information fields for the template
    required_info = template["info"]
    
    # Check if there is enough information
    missing_info = []
    for key in required_info:
        if key not in info or info[key] is None:
            missing_info.append(key)
    
    # If there is missing information, return info_not_found template
    if missing_info:
        return template.get("info_not_found", "I'm sorry, I couldn't find the information you need.")
    
    # Select the appropriate sentiment template
    if sentiment not in template:
        sentiment = "neutral"  # Use neutral as default
    
    response_template = template[sentiment]
    
    # Use string formatting to fill in the information
    try:
        # Create a format dictionary, only containing the fields needed for the template
        format_dict = {}
        for key in required_info:
            if key in info:
                format_dict[key] = info[key]
        
        # Use format method to fill in the template
        formatted_response = response_template.format(**format_dict)
        return formatted_response
        
    except KeyError as e:
        # If formatting fails, return info_not_found
        return template.get("info_not_found", f"I'm sorry, I couldn't process your request: {str(e)}")
    except Exception as e:
        # Other exception handling
        return template.get("info_not_found", "I'm sorry, an error occurred while processing your request.")