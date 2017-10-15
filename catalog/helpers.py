from catalog.models import *
import operator


######################################################################
# Find Similar Internships for user
###################################
# -Todo: Fix db n+1 search queries problem in functions

def find_favorite_int_category(user):
    id = user.id
    fav_categories = {}
    intviews_of_user = Int_View.objects.filter(session_key_or_user_id=id).select_related(
        'rel_int__category').values()  # TODO Fix new way
    for view in intviews_of_user:
        category = view.rel_int.category  # n+1 here for example
        if category in fav_categories:
            fav_categories[category] += 1
        else:
            fav_categories[category] = 1
    fav_categories_sorted = sorted(fav_categories.items(), key=operator.itemgetter(1), reverse=True)
    return fav_categories_sorted[:3]


# Removes the unnecessary words in internship titles that doesn't represent similarity in any way
# Note that this method returns the words in capitalized form!
def words_to_search(target_title):
    expandables_to_exclude = ('Staj', 'ilan', 'İlan', 'imkan', 'İmkan', 'uzman', 'İçin', 'için')
    directs_to_exclude = ('ve', 'ile', 'İle', 'iş', 'İş')
    title_words = target_title.split(" ")
    filtered_words = []
    for word in title_words:
        word = word.upper()
        is_exception = False
        for exception in expandables_to_exclude:
            if not word.find(exception.upper()) == -1:
                is_exception = True
        for exception in directs_to_exclude:
            if word == exception.upper():
                is_exception = True
        if not is_exception:
            filtered_words.append(word.upper())

    # list(filter(lambda x: x.upper() not in new_directs_to_exclude and len(
    #     list(filter(lambda exception: x.upper().find(exception.upper()) != -1, new_expandables_to_exclude))) == 0,
    #             splitted_metin)) FIXME try this HIGHER ORDER FUNCTIONS?

    return filtered_words


def find_recommended_ints(target_int,
                          user):  # TODO [ASK] userı paramater olarak view de mi sunmalı yoksa liseli manytomany model field yapıp giriş yapınca update mi etmeli
    category = target_int.category
    location_words = target_int.location.upper().split(" ")
    type = target_int.type
    if user:
        fav_category = find_favorite_int_category(user)
    title_words = words_to_search(target_int.name)

    all_ints = Internship.objects.all()
    int_scores = {}
    for internship in all_ints:
        final_score = 0

        curr_category = internship.category
        # Does the category match with the current one's
        same_category_point = 5 if category == curr_category else 0 # TODO ternary operator

        cat_score = 0
        if user:
            # Is the category one of the user's favorites
            if curr_category == fav_category[0][0]:
                cat_score = 8
            elif curr_category == fav_category[1][0]:
                cat_score = 5
            elif curr_category == fav_category[2][0]:
                cat_score = 3

        current_title_words = words_to_search(internship.name)
        word_score = 0
        for word in title_words:
            for curr_word in current_title_words:
                if not word.find(curr_word) == -1 or not curr_word.find(word) == -1:
                    word_score += 3

        # Check if there are similar words in location infos
        location_match = False
        for loc in location_words:
            if not internship.location.find(loc) == -1:
                location_match = True
        if location_match:
            location_score = 3
        else:
            location_score = 0

        # Compare internship type (Paid / part-time etc)
        if internship.type == type:
            type_score = 2
        else:
            type_score = 0

        final_score = same_category_point + cat_score + word_score + location_score + type_score
        int_scores[internship] = final_score
    int_scores = sorted(int_scores.items(), key=operator.itemgetter(1), reverse=True)
    top_scorers = []
    for x in range(0, 5):
        internship = int_scores[x][0]
        top_scorers.append(internship)

    return top_scorers

    ####################################################################################
