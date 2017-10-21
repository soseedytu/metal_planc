from metal.models.Codes import Tag


class TagRepository(object):
    def get_tags_all(self):
        querySet = Tag.objects.filter(Status__exact=1)
        return querySet

    def get_tags_by_id_arrary(self, tag_ids):
        queries = {}
        for tag_id in tag_ids:
            key = '{0}__{1}'.format('Id', 'exact')
            queries[key] = tag_id

        query = queries.pop
        for item in queries:
            query |= item

        querySet = Tag.objects.filter(query)

        return querySet
