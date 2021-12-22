from collections import OrderedDict

"Capacity of LRU Cache"
N=3;

"Define LRU Cache with OrderedDict using doubly linnked list as underline stucture"
cache = OrderedDict();

"Fake fuction to build book info only for testing purpose"
def get_book_info(isbn) :
    return {"Title", "Author", "Language"};

"Q1 Using Python"
def get_book_info_with_cache(isbn):
    "If exist in cache, obtain from cache"
    if isbn in cache:
        cache.move_to_end(isbn); "Update position to LRU to optimise query speed"
        return cache[isbn];
    else:
        book = get_book_info(isbn);  "If not cached, call real fuction to obtain book object"
        cache[isbn] = book;         "Store in cache"
        cache.move_to_end(isbn);    "Update position to LRU to optimise query speed"
        if len(cache) > N:
            cache.popitem(last = False);    "Remove first item from cache if reach capaticy"
        return book;


"Testing:"
get_book_info_with_cache("1");
print(cache);
get_book_info_with_cache("2");
print(cache);
get_book_info_with_cache("3");
print(cache);
get_book_info_with_cache("2");
print(cache);
get_book_info_with_cache("4");
print(cache);
get_book_info_with_cache("3");
print(cache);
get_book_info_with_cache("5");
print(cache);
