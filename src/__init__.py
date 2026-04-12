from fastapi import FastAPI
from src.auth.routes import auth_router
from src.books.routes import book_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from .errors import register_all_errors
from .middleware import register_middleware
from fastapi.responses import HTMLResponse


version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix =f"/api/{version}"

app = FastAPI(
    title="BookCrust",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)

register_middleware(app)

@app.get("/")
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bookcrust API | Home</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Inter', sans-serif; }
            .glass {
                background: rgba(255, 255, 255, 0.03);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
        </style>
    </head>
    <body class="bg-slate-950 text-slate-200 min-h-screen flex items-center justify-center p-6">
        
        <div class="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
            <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-blue-900/20 rounded-full blur-[120px]"></div>
            <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-900/20 rounded-full blur-[120px]"></div>
        </div>

        <div class="max-w-2xl w-full text-center space-y-8 glass p-12 rounded-3xl shadow-2xl">
            <div class="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-tr from-blue-500 to-purple-600 rounded-2xl shadow-lg mb-4">
                <svg xmlns="https://www.w3.org/2000/svg" class="h-10 w-10 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
            </div>

            <h1 class="text-5xl font-bold tracking-tight text-white bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">
                Bookcrust API
            </h1>
            
            <p class="text-lg text-slate-400 max-w-md mx-auto leading-relaxed">
                Welcome to the high-performance backend for Bookcrust. Fully automated, orchestrated, and ready for integration.
            </p>

            <div class="flex flex-col sm:flex-row gap-4 justify-center items-center pt-4">
                <a href="/api/v1/docs" class="px-8 py-3 bg-white text-slate-950 font-semibold rounded-xl hover:bg-blue-400 hover:text-white transition-all duration-300 shadow-xl shadow-white/5">
                    View Documentation
                </a>
                <a href="https://github.com" target="https://github.com/siddiquesahabaj/bookcrust" class="px-8 py-3 glass text-white font-medium rounded-xl hover:bg-white/10 transition-all duration-300">
                    GitHub Repo
                </a>
            </div>

            <div class="pt-8 border-t border-white/5 flex justify-center gap-6 text-sm text-slate-500 uppercase tracking-widest">
                <span class="flex items-center gap-2">
                    <span class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
                    System Active
                </span>
                <span>v1.0.0</span>
            </div>
        </div>
    </body>
    </html>
    """

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"{version_prefix}/tags", tags=["tags"])
