const db = require('./db');
const { ApolloError } = require('apollo-server-express');

const lightsCyclePlan = 'light_plan';

export default {
  Query: {
    setting: (parent: any, args: { name: string }): object => {
      const text = 'SELECT * FROM user_settings WHERE name = $1';
      const values = [args.name];
      return db
        .query(text, values)
        .then((res: any) => {
          const row = res.rows[0];
          return row;
        })
        .catch((e: any) => {
          console.log(e);
          throw new ApolloError(e.message);
        });
    },
    lightPlan: (): object => {
      const text = 'SELECT * FROM user_settings WHERE name = $1';
      const values = [lightsCyclePlan];
      return db
        .query(text, values)
        .then((res: any) => {
          const row = res.rows[0];
          return row;
        })
        .catch((e: any) => {
          console.log(e);
          throw new ApolloError(e.message);
        });
    },
  },
  Mutation: {
    updateLightPlan: (parent: any, args: { name: string; value: JSON }): object => {
      const text = 'UPDATE user_settings SET value = $1 WHERE name= $2 RETURNING *';
      const values = [JSON.stringify(args.value), lightsCyclePlan];

      return db
        .query(text, values)
        .then((res: any) => {
          const row = res.rows[0];
          return row;
        })
        .catch((e: any) => {
          console.log(e);
          throw new ApolloError(e.message);
        });
    },
  },
};
