from .categories import router as categories_router
from .products import router as products_router

# Optionally, you can create a list of all routers for easy inclusion in the main FastAPI app
all_routers = [
    categories_router,
    products_router,
]