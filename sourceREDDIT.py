import random
import praw

reddit: praw.Reddit = praw.Reddit(
    client_id="9EXDeyozdzMuhb1COAqnpQ",
    client_secret="dU1J0681cmtNo2Pkx9JAgK9uMxgqNA",
    user_agent="Test app for camels and chickens by u/Camel-of_Chicken",
    username="Camel-of_Chicken",
    password="Thisn0tThepass"
)

TEXT_ONLY_SUBREDDITS: list = ["TalesFromTechSupport", "TalesFromThePizzaGuy", "TalesFromRetail", "LifeOfNorman",
                              "PettyRevenge"]
GME_SUBREDDITS: list = ["Superstonk", "GME", "wallstreetbets", "GMEJungle"]
SUBREDDIT_STRING: str = ""
for subreddit in GME_SUBREDDITS:
    SUBREDDIT_STRING += subreddit + "+"

subreddit = reddit.subreddit("superstonk")
submission = subreddit.random()


def new_chosen_submission(submis_id) -> dict:
    """Return an info dictionary of a chosen submission from reddit."""
    submis = reddit.submission(id=submis_id)
    submission_info_dict = {
        'id': submis.id,
        'title': submis.title,
        'author': submis.author,
        'num_comments': submis.num_comments,
        'comments': submis.comments,
        'score': submis.score,
        'upvote_ratio': submis.upvote_ratio,
    }
    return submission_info_dict


def create_IDUTC() -> (str, str):
    """Picks a random submission from a subreddit and returns an idutc tuple."""
    chosen_subreddit = reddit.subreddit(random.choice(TEXT_ONLY_SUBREDDITS))
    picked_submission = chosen_subreddit.random()
    use_id = picked_submission.id
    use_utc = int(picked_submission.created_utc)
    return use_id, use_utc
