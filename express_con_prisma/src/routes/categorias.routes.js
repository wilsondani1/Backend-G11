
import { Router } from "express";
import { crearCategoria } from "../controllers/categorias.controller.js";
import { listarCategorias } from "../controllers/categorias.controller.js";
import { devolverCategoria } from "../controllers/categorias.controller.js";
import { actualizarCategoria } from "../controllers/categorias.controller.js";
import { eliminarCategoria } from "../controllers/categorias.controller.js";

export const categoriaRouter = Router();

categoriaRouter.route('/categorias').post(crearCategoria).get(listarCategorias);
categoriaRouter
.route('/categorias/:id')
.get(devolverCategoria)
.patch(actualizarCategoria)
.put(actualizarCategoria)
.delete(eliminarCategoria);
