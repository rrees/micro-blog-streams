import flask

from rrees_tag_manager import tags as tag_manager

from app.auth_password.decorators import login_required
from app import forms
from app.repositories import posts as posts_repository
from app.repositories import topics as topics_repository


@login_required
def new_post():
    new_post_form = forms.Post(flask.request.form)

    if new_post_form.validate():
        topic_id = new_post_form.topic_id.data
        tags = tag_manager.process(new_post_form.tags.data)

        url = None

        if new_post_form.url.data:
            url = new_post_form.url.data

        new_post = posts_repository.create(
            new_post_form.title.data,
            new_post_form.content.data,
            topic_id=topic_id,
            tags=tags,
            url=url,
        )

        if topic_id:
            return flask.redirect(flask.url_for("topic", topic_id=topic_id))

        return flask.redirect(flask.url_for("recent"))


@login_required
def new_topic():
    new_topic_form = forms.Topic(flask.request.form)

    if new_topic_form.validate():
        new_topic = topics_repository.create(
            new_topic_form.title.data, new_topic_form.description.data
        )
        return flask.redirect(flask.url_for("topics"))


@login_required
def edit_post(post_id):
    edit_post_form = forms.Post(flask.request.form)
    if edit_post_form.validate():
        update_data = {
            "id": post_id,
            "title": edit_post_form.title.data,
            "content": edit_post_form.content.data,
            "tags": tag_manager.process(edit_post_form.tags.data),
        }

        if edit_post_form.url.data:
            update_data["url"] = edit_post_form.url.data

        posts_repository.update_post(update_data)
        return flask.redirect(flask.url_for("post", post_id=post_id))

    flask.abort(400, "Form information was invalid")


@login_required
def edit_topic(topic_id):
    edit_topic_form = forms.Topic(flask.request.form)
    if edit_topic_form.validate():
        update_data = {"topic_id": topic_id, "title": edit_topic_form.title.data}

        if edit_topic_form.description.data:
            update_data["description"] = edit_topic_form.description.data

        topics_repository.update(update_data)

        return flask.redirect(flask.url_for("topic", topic_id=topic_id))
    flask.abort(400, "Form information incorrect")


@login_required
def add_post_to_topic(post_id):
    topic_id_form = forms.TopicId(flask.request.form)

    if topic_id_form.validate():
        topic_id = topic_id_form.topic_id.data

        topics_repository.add_post_to_topic(post_id, topic_id)

        return flask.redirect(flask.url_for("edit_post_topics", post_id=post_id))

    flask.abort(400, "Form information incorrect")


@login_required
def remove_topic_from_post(post_id):
    topic_id_form = forms.TopicId(flask.request.form)

    if topic_id_form.validate():
        topic_id = topic_id_form.topic_id.data

        posts_repository.remove_topic(post_id, topic_id)

        return flask.redirect(flask.url_for("edit_post_topics", post_id=post_id))

    flask.abort(400, "Form information incorrect")


@login_required
def delete_topic(topic_id):
    topics_repository.delete(topic_id)

    return flask.redirect(flask.url_for("topics"))


@login_required
def archive_topic(topic_id):
    return topic_active_status(topic_id, False)


@login_required
def unarchive_topic(topic_id):
    return topic_active_status(topic_id, True)


def topic_active_status(topic_id, active_flag):
    topics_repository.active_flag(topic_id, active_flag)

    return flask.redirect(flask.url_for("topic", topic_id=topic_id))
