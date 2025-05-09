import { products } from "./products";
import { Product } from "./models/Product";
import { Stock } from "./models/Stock";

function createProductList() {
  let product_list = [];

  for (let product in products) {
    let stock = Stock.getCurrentStock(product.dish);

    product_list.push(
      new Product(product.dish, product.image, product.description, stock)
    );
  }
}
