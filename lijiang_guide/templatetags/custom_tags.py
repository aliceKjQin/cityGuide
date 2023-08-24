from django import template

register = template.Library()


# create this custom tag to generate a range of numbers based on the review.star_rating value, allowing to loop through and display the correct number of filled stars.
@register.filter
def get_star_rating_range(value):
    return range(value)