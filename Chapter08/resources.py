from protorpc import messages
from protorpc import message_types


class CheckListItemRepr(messages.Message):
    title = messages.StringField(1)
    checked = messages.BooleanField(2)


class NoteRepr(messages.Message):
    key = messages.StringField(1)
    title = messages.StringField(2)
    content = messages.StringField(3)
    date_created = message_types.DateTimeField(4)
    checklist_items = messages.MessageField(CheckListItemRepr, 5, repeated=True)
    files = messages.StringField(6, repeated=True)


class NoteCollection(messages.Message):
    items = messages.MessageField(NoteRepr, 1, repeated=True)


class NoteFileRepr(messages.Message):
    key = messages.StringField(1)
    name = messages.StringField(2)
    url = messages.StringField(3)
    thumbnail_url = messages.StringField(4)


class NoteFileCollection(messages.Message):
    items = messages.MessageField(NoteFileRepr, 1, repeated=True)
