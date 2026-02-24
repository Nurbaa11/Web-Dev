import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home';
import { UsersComponent } from './pages/users/users';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'users', component: UsersComponent },
];