
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
};
export const devolverCategoria = async (req,res) =>{
  const {id} = req.params;
  const categoria = await Prisma .categoria.findFirst({
    where:{
      id:+id,
    },
  });
  if (!categoria) {
    res.status(400).json({
      message:"la categoria no existe "
    });
  }

  return res.status(200).json({
    content : categoria,
  });
};

export const actualizarCategoria = async (req,res) =>{
 const data = req.body;
 const {id} = req.params;

  const categoria = await Prisma .categoria.findFirst({
    where:{
      id:+id,
    },

    select:{
      id:true,
    },
  });

  if (!categoria) {
    res.status(400).json({
      message:"la categoria no existe "
    });
  }

   const categriaActualizada = await Prisma .categoria.update({
    where:{
      id:categoria.id,
    },
    data:data,
   });

   return res.json({
    message : "categoria actualiada exitosamente",
    content : categriaActualizada,
   });
  };


  export const eliminarCategoria = async (req,res) =>{
    const {id} = req.params;

    const categoria = await Prisma .categoria.findFirst({
      where:{
        id:+id,
      },
      select:{
        id:true,
      },
    });

    if (!categoria) {
      res.status(400).json({
        message:"la categoria no existe "
      });
    }

    const categoriaEliminada = await Prisma .categoria.delete({
        where:{id:+id},
        });
        return res.json({
          message :"categoria eliminada exitosamente",
          content :categoriaEliminada,
        });
      };

