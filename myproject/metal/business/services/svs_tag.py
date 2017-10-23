import asyncio
from metal.business.repository.repo_tag import TagRepository


class TagService(object):

    async def get_tags_all(self, future):
        repo = TagRepository()
        queryset = repo.get_tags_all()
        result = queryset.values('Id', 'TagName')
        future.set_result(result)
        #return result

    def get_tags_text_from_arrary(self, tags):
        result = ""

        if(tags is None):
            return result

        repo = TagRepository()
        tag_objects = repo.get_tags_by_id_arrary(tags)

        if (tag_objects is None):
            return result

        for tag in tag_objects:
            if(result is not ""):
                result = result + ";"

            result = result + '{0}{1}{2}'.format('#', tag.TagName, "#")
        #end for loop#

        return result


