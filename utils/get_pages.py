import json
import os
from tqdm import tqdm


def get_pages(pages: int) -> list:
    links =  [f'''https://24.kg/page_{i}/''' for i in tqdm(range(1, pages + 1))]

    if not os.path.exists('outputs'):
        os.mkdir('outputs')
        
    with open('outputs/links.json', 'w') as f:
        json.dump(links, f, indent = 4)

    print()
    print('=' * 50)
    print(f'{pages} links requested')
    print(f'The list of links has been saved in outputs/links.json')
    print('=' * 50)
    print()
    
    return links