Rails.application.routes.draw do
  root "pages#home"
  get "/tech", to: "pages#tech"
  get "/somos", to: "pages#somos"
end
