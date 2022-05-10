import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }
  // Generic Http Get method function for all api calls
  getRecord(endpointurl: any, params: any) {
    return new Promise((resolve, reject) => {
      return this.http.get<[]>(endpointurl, params).subscribe((res) => {
        resolve(res);
      }, err => {

        reject(err);
      });

    });

  }
  // Generic Http Post method function for all api calls
  postRecord(endpointurl: any, params: any) {
    return new Promise((resolve, reject) => {
      return this.http.post<[]>(endpointurl, params).subscribe((res) => {
        resolve(res);
      }, err => {

        reject(err);
      });

    });

  }
}
