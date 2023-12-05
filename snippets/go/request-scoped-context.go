package main

import (
	"context"
	"fmt"
	"net/http"
)

type FooKey string

const foo FooKey = "foo"

func MyTestMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		ctxWithFooBar := context.WithValue(r.Context(), foo, "bar")
		rWithFooBar := r.WithContext(ctxWithFooBar)
		next.ServeHTTP(w, rWithFooBar)
	})
}

func Hi(w http.ResponseWriter, r *http.Request) {
	value := r.Context().Value(foo)
	fmt.Fprint(w, value)
}

func main() {
	fmt.Println("Starting server...")
	serverMux := http.NewServeMux()
	serverMux.Handle("/", MyTestMiddleware(http.HandlerFunc(Hi)))
	http.ListenAndServe(":8082", serverMux)
}
