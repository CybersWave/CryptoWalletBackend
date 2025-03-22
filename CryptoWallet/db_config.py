from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# postgres = {
#     'default': {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": config('PG_NAME'),
#         "USER": config('PG_USER'),
#         "PASSWORD": config('PG_PASSWORD'),
#         "HOST": config('PG_HOST'),
#         "PORT": config('PG_PORT', '5432'),
#         'ATOMIC_REQUESTS': True,
#     }
# }


sqlite3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


