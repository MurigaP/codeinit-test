import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { api_supported_errors } from './api_errors';
import { NotificationService } from '../services/notification.service';

@Injectable()
export class ErrorInterceptor implements HttpInterceptor {

  constructor(public notificationService: NotificationService) { }

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    return next.handle(request).pipe(
      tap((event: HttpEvent<any>) => {
      }, (err: any) => {
        if (err instanceof HttpErrorResponse) {
          if (err.status === 403 || err.status === 401 || err.status === 400) {
            let error = err.error;
            let responseError = error?.error || "SystemError";
            let errorMessage = api_supported_errors[responseError];
            this.notificationService.showSweetAlert("An error occurred", errorMessage, "error");



            console.log("errorMessage",)
          }
        }
      }
      )
    );
  }
}

