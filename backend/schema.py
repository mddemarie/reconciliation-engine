import graphene

import backend.reconciliation.schema


class Query(backend.reconciliation.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
