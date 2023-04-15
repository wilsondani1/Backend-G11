
import { Prisma } from "../prisma.js";

export const crearCategoria = async (req, res) => {
  const body = req.body;

  const resultado = await Prisma.categoria.create({
    data: body,
  });

  console.log(resultado);

  res.status(201).json({
    message: "La categoria se creo exitosamente",
  });
};

export const listarCategorias = async (req,res) => {
  const categorias = await Prisma.categoria.findMany();
  res.json({
    content : categorias,
  });
}