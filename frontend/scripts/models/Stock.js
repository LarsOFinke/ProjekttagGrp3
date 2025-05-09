import { get_current_stock } from "../api";

export class Stock {
  constructor() {
    this.stock = get_current_stock();
  }
}
