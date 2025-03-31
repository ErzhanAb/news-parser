from utils.get_pages import get_pages
from utils.get_dataset import get_dataset
from utils.get_top import get_top


links = get_pages(int(input('How many pages to parse? ')))


dataset = get_dataset(links)


get_top(dataset, int(input('How many top words do you want to retrieve? ')))