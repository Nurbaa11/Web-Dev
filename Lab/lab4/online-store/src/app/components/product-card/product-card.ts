import { Component, input } from '@angular/core';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-card',
  standalone: true,
  templateUrl: './product-card.html',
  styleUrl: './product-card.css',
})
export class ProductCardComponent {
  product = input.required<Product>();

  get whatsappUrl(): string {
    const link = this.product().link;
    return `https://wa.me/?text=${encodeURIComponent('Check out this product: ' + link)}`;
  }

  get telegramUrl(): string {
    const link = this.product().link;
    const name = this.product().name;
    return `https://t.me/share/url?url=${encodeURIComponent(link)}&text=${encodeURIComponent(name)}`;
  }
}