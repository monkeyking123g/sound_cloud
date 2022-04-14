import os

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """ Building a path to a file, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def get_path_upload_cover_album(instance, file):
    """ Building a path to a file, format: (media)/album/user_id/photo.jpg
    """
    return f'album/user_{instance.user.id}/{file}'


def get_path_upload_cover_playlist(instance, file):
    """ Building a path to a file, format: (media)/playlist/user_id/photo.jpg
    """
    return f'playlist/user_{instance.user.id}/{file}'


def get_path_upload_track(instance, file):
    """ Building a path to a file, format: (media)/track/user_id/audio.pm3
    """
    return f'track/user_{instance.user.id}/{file}'


def get_path_upload_cover_track(instance, file):
    """ Building a path to a file, format: (media)/track/cover/user_id/photo.jpg
    """
    return f'track/cover/user_{instance.user.id}/{file}'


def validate_size_image(file_obj):
    """ Check size file
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Maximum file size {megabyte_limit}MB")


def delete_old_file(path_file):
    """ Delete old file
    """
    if os.path.exists(path_file):
        os.remove(path_file)
