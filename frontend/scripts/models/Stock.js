import { fetch_data } from "../api";
export class Stock {
  constructor() {
    this.stock = this.get_current_stock();
  }

  async get_current_stock() {
    return await fetch_data("stock");
  }
}
