from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Siz obuna boldingiz !!!',
        'Sizni royxatga oldik! Keyingi safar login qilib kirsangiz boladi !',
        'your@gmail.com',
        [user_email],
        fail_silently=False,
    )
