import graphene

import CookBook.schema


class Query(CookBook.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)