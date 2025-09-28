from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import posts_schemas
from ..models import Posts

# create new post


class PostService():
    def __init__(self, db: AsyncSession):
        self.db=db

    async def create_post(
        self,
        post_data: posts_schemas.PostCreate,
        author_id: str,
    ):
        db_post = Posts(
            title= post_data.title,
            content = post_data.content,
            author_id=author_id
        )

        self.db.add(db_post)
        await self.db.commit()
        await self.db.refresh(db_post)
        return db_post

    # get
    async def get_all_post(
        self
    ):
        res = await self.db.execute(select(Posts))
        all_posts = res.scalars().all()
        return all_posts
    # delete


