import httpx
from fastapi import APIRouter
from bs4 import BeautifulSoup

router = APIRouter(
    prefix="/crawler",
    tags=["Crawler"]
)

routes = [
    "/{website}",
    "/{website}/classes",
    "/{website}/{item}/{class}/all",
    "/{website}/{item}/{class}/one",
    "/{website}/{item}/{attribute}/all",
    "/{website}/{item}/{attribute}/one",
    "/{website}/{item}/{class}/{attribute}/all",
    "/{website}/{item}/{class}/{attribute}/one"
]


@router.get("/")
def index():
    return routes


@router.get("/{website}")
def crawl_entire_website(website):
    return httpx.get("https://"+website).text


@router.get("/{website}/classes")
def classes(website):
    class_list = set()
    r = httpx.get("https://"+website)
    soup = BeautifulSoup(r.content, "html.parser")
    tags = {tag.name for tag in soup.find_all()}
    for tag in tags:
        for i in soup.find_all(tag):
            if i.has_attr("class"):
                if len(i['class']) != 0:
                    class_list.add(" ".join(i['class']))
    return class_list


@router.get("/{website}/{item}/{attribute}/all")
def get_all_items_by_attributes(website, item, attribute):
    r = httpx.get("https://"+website).text
    soup = BeautifulSoup(r, "html.parser")
    return soup.find_all(item)[attribute]


@router.get("/{website}/{item}/{attribute}/one")
def get_one_items_by_attributes(website, item, attribute):
    r = httpx.get("https://"+website).text
    soup = BeautifulSoup(r, "html.parser")
    return soup.find(item)[attribute]


@router.get("/{website}/{item}/{classname}/all")
def get_all_items_by_classname(website, item, classname):
    r = httpx.get("https://"+website).text
    soup = BeautifulSoup(r, "html.parser")
    return soup.find_all(item, class_=classname)


@router.get("/{website}/{item}/{classname}/one")
def get_one_items_by_classname(website, item, classname):
    r = httpx.get("https://"+website).text
    soup = BeautifulSoup(r, "html.parser")
    return soup.find(item, class_=classname)


@router.get("/{website}/{item}/{class}/{attribute}/all")
def get_all_items_attributes_by_classname(website, item, classname, attribute):
    r = httpx.get("https://"+website).text
    soup = BeautifulSoup(r, "html.parser")
    return soup.findAll(item, class_=classname)[attribute]


@router.get("/{website}/{item}/{class}/{attribute}/one")
def get_one_items_attributes_by_classname(website, item, classname, attribute):
    r = httpx.get("https://"+website).text
    soup = BeautifulSoup(r, "html.parser")
    return soup.find(item, class_=classname)[attribute]
