import Express from 'express';
import { createClient, print } from 'redis';
import { promisify } from 'util';

const app = Express();
const redisClient = createClient();

const listProducts = [

  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }

];

function getItemById (id) {
  for (const item of listProducts) {
    if (item.Id === id) {
      return item;
    }
  }
  return null;
}

function reserveStockById (itemId, stock) {
  redisClient.set(`item.${itemId}`, stock, print);
}

async function getCurrentReservedStockById (itemId) {
  const getAsync = promisify(redisClient.get).bind(redisClient);
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

app.get('/list_products', (req, res) => {
  const items = listProducts.map((product) => ({
    itemId: product.Id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  }));
  res.json(items);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (item) {
    return res.json(item);
  } else {
    return res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  if (item.stock < 1) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  reserveStockById(itemId, 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(1245);

export default app;
