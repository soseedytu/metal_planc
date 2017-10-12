from metal.models.Codes import Tag


class TagRepository(object):

    def get_tags_all(self):
        querySet = Tag.objects.filter(Status__exact=1)
        return querySet

