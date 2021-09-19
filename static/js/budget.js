const items = document.getElementById('items');
var num_items = 0;

const create_div = (item='', cost='') => {
    const item_div = document.createElement('div');
    item_div.className = 'form-group my-3 d-flex justify-content-center';
    item_div.id = `item-${num_items}`;
    item_div.innerHTML += `
            <input type="text" id="item-${num_items}-name" class="form-control" placeholder="Item" value="${item}" required>
            <input type="number" id="item-${num_items}-cost" class="form-control" placeholder="Cost" value="${cost}" required>
            <button onclick="remove_item('item-${num_items}');" class="btn btn-primary ms-2">-</button>
    `;
    items.append(item_div);
}

const set_form = () => {
    if (budget !== {}) {
        document.getElementById('budget-value-wrapper').innerHTML = `
            <input type="number" id="budget-value" class="form-control" placeholder="Budget Value" value="${budget['budget_value']}" required>    
        `;
        for (let item in budget['items']) {
            num_items++;
            create_div(item, budget['items'][item]);
        }
    } else {
        num_items++;
        document.getElementById('budget-value-wrapper').innerHTML = `
            <input type="number" id="budget-value" class="form-control" placeholder="Budget Value" required>
        `;
        create_div();
    }
}

set_form();

const add_item = (event) => {
    num_items++;
    create_div();
    event.preventDefault();
}

document.getElementById('add-btn').addEventListener('click', add_item);

const remove_item = (id) => {
    document.getElementById(id).remove();
    num_items--;
}

// Form submit
const budget_form = document.getElementById('budget-form');

budget_form.addEventListener('submit', addFormToBackend);

async function addFormToBackend(event) {
    event.preventDefault();

    let items = {};
    for (let i = 1; i <= num_items; i++) {
        let item_name = document.getElementById(`item-${i}-name`).value;
        let item_cost = document.getElementById(`item-${i}-cost`).value;
        items[item_name] = item_cost;
    }

    budget = {
        'budget_value': document.getElementById('budget-value').value,
        'items': items
    }

    const result = await fetch('/api/create-budget/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(budget)
    }).then((res) => res.json());
    budget = result;
}
