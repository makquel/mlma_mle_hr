# Inventory Management System

## Machine Learning marketing and advertising

Template for Machine Learning Engineer problem set (Python version)

### Problem statement:

Lets suppose that Mercado Libre is now offering on its marketplace (MercadoLibre fresh market) a new service of groceries and provisions that are available, at least for now, in certain regions in order to keep the same-day shipping policy. Behind that capability there is a complex supply chain system that has been tunned based on the test pilot. However, is a huge concern that this new capability has potentially some pitfalls regarding the stock management for fresh and perishable products.

In order to optimize this service, it's been required, by the logistics department, to create predictive model that would allow us to lay in sotck in order to fufill our customers needs, without compromising their experience on our market place, but keep our losing margin very low.

As a machine learning engineer you've been requested to create a computational model of how inventory management system works, in order to help our data science engineers on the modeling process. This system relies on two methods that deal with items/products.

- FIFO (“First-In, First-Out”) seeks to value inventory so the business is less likely to lose money when products expire or become obsolete;
- LIFO (“Last-In, First-Out”) is better for nonperishable goods and uses current prices to calculate the cost of goods sold.

### Hands-on

Both of them are different approaches to organizing and manipulating the data structure in computing, and furthermore, we've come with the ideia that and inventory could be modeled as a Buffer. Thus we'll build this data model from a base class provided for us.

In order to keep this coding problem real, we introduce, off-the-shelf a few auxiliary classes for buffer implementation, debugging and testing.

Item related data class

```python
@unique
class State(Enum):
    """
    active: currently in stock
    inactive: out of stock
    """

    active = "active"
    inactive = "inactive"


class Item(NamedTuple):
    id: str
    price: float
    state: State
```

Defintion for generation random items

```python
def generate_item() -> Tuple:
    def randomDigits(digits: int) -> int:
        lower = 10 ** (digits - 1)
        upper = 10**digits - 1
        return random.randint(lower, upper)

    retail_price = round(random.uniform(10.0, 100.0), 2)
    id = "MLX" + str(randomDigits(6))
    return (id, retail_price, State.active)
```
