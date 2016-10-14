import fresh_tomatoes
import media

PULP_FICTION = media.Movie("Pulp Fiction",
                           "https://upload.wikimedia.org/wikipedia/en/"
                           "thumb/8/82/Pulp_Fiction_cover.jpg/"
                           "220px-Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                           "Quentin Tarantino",
                           "John Travolta, Uma Thurman, Samuel L. Jackson",
                           "1994", False, None)

SHAUN_OF_THE_DEAD = media.Movie("Shaun of the Dead",
                                "https://upload.wikimedia.org/wikipedia/en/"
                                "thumb/e/ec/Shaun-of-the-dead.jpg/"
                                "220px-Shaun-of-the-dead.jpg",
                                "https://www.youtube.com/watch?v=z-lmF5DAssU",
                                "Edgar Wright",
                                "Simon Pegg, Nick Frost, Kate Ashfield",
                                "2004", False, None)

SOCIAL_NETWORK = media.Movie("Social Network",
                             "https://upload.wikimedia.org/wikipedia/en/"
                             "thumb/7/7a/Social_network_film_poster.jpg/"
                             "220px-Social_network_film_poster.jpg",
                             "https://www.youtube.com/watch?v=lB95KLmpLR4",
                             "David Fincher",
                             "Jesse Eisenberg, Andrew Garfield,\
                              Justin Timberlake",
                             "2010", False, None)

HOT_FUZZ = media.Movie("Hot fuzz",
                       "https://upload.wikimedia.org/wikipedia/en/"
                       "thumb/c/c9/HotFuzzUKposter.jpg/"
                       "250px-HotFuzzUKposter.jpg",
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4",
                       "Edgar Wright",
                       "Simon Pegg, Nick Frost, Martin Freeman",
                       "2007", False, None)

EDWARD_SCISSORHANDS = media.Movie("Edward Scissorhands",
                                  "https://upload.wikimedia.org/wikipedia/en/"
                                  "thumb/3/3b/Edwardscissorhandsposter.JPG/"
                                  "220px-Edwardscissorhandsposter.JPG",
                                  "https://www.youtube.com/"
                                  "watch?v=M94yyfWy-KI",
                                  "Tim Burton",
                                  "Johnny Depp, Winona Ryder, Dianne Wiest",
                                  "1990", False, None)

AMERICAN_HUSTLE = media.Movie("American Hustle",
                              "https://upload.wikimedia.org/wikipedia/en/"
                              "thumb/8/85/American_Hustle_2013_poster.jpg/"
                              "220px-American_Hustle_2013_poster.jpg",
                              "https://www.youtube.com/watch?v=ST7a1aK_lG0",
                              "David O. Russell",
                              "Christian Bale, Amy Adams, Bradley Cooper",
                              "2013", False, None)

AMERICAN_PSYCHO = media.Movie("American Psycho",
                              "https://upload.wikimedia.org/wikipedia/en/"
                              "thumb/6/63/Americanpsychoposter.jpg/"
                              "220px-Americanpsychoposter.jpg",
                              "https://www.youtube.com/watch?v=2GIsExb5jJU",
                              "Mary Harron",
                              "Christian Bale, Justin Theroux, Josh Lucas",
                              "2000", False, None)


movies = [PULP_FICTION, SHAUN_OF_THE_DEAD, SOCIAL_NETWORK, HOT_FUZZ, EDWARD_SCISSORHANDS, AMERICAN_HUSTLE, AMERICAN_PSYCHO]

fresh_tomatoes.open_movies_page(movies)