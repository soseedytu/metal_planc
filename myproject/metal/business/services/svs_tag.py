from metal.business.repository.repo_tag import TagRepository


class TagService(object):

    def get_tags_all(self):
        repo = TagRepository()
        queryset = repo.get_tags_all()
        result = queryset.values('Id', 'TagName')
        return result




