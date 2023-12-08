from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime, movie_id: int,
                         cinema_hall_id: int) -> QuerySet:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall_id=cinema_hall_id,
                                       movie_id=movie_id)


def get_movies_sessions(session_date: Optional[datetime] = None) -> QuerySet:
    if session_date is None:
        return MovieSession.objects.all()

    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None, cinema_hall_id: Optional[int] = None
                         ) -> QuerySet:
    queryset = MovieSession.objects.filter(id=session_id)
    if show_time is not None:
        queryset.update(show_time=show_time)

    if movie_id:
        queryset.update(movie_id=movie_id)

    if cinema_hall_id:
        queryset.update(cinema_hall_id=cinema_hall_id)

    return queryset


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()