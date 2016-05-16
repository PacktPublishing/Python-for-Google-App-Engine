from google.appengine.ext import ndb


class CheckListItem(ndb.Model):
    title = ndb.StringProperty()
    checked = ndb.BooleanProperty(default=False)


class Note(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty(required=True)
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    checklist_items = ndb.StructuredProperty(CheckListItem, repeated=True)
    files = ndb.KeyProperty("NoteFile",
                            repeated=True)

    @classmethod
    def owner_query(cls, parent_key):
        return cls.query(ancestor=parent_key).order(
            -cls.date_created)


class NoteFile(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    url = ndb.StringProperty(indexed=False)
    thumbnail_url = ndb.StringProperty(indexed=False)
    full_path = ndb.StringProperty(indexed=False)


class UserLoader(ndb.Model):
    user = ndb.UserProperty()
