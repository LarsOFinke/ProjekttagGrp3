import { fetchData } from "../api";
export class Stock {
  constructor() {
    this.stock = this.getTotalStock();
  }

  async getTotalStock() {
    return await fetchData("stock");
  }

  getCurrentStock(item) {
    return this.stock[item];
  }
}
