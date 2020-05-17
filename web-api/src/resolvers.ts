const db = require('./db');
const { ApolloError } = require('apollo-server-express');

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
    lightCycle: (): object => {
      const text = 'SELECT * FROM user_settings WHERE name = $1';
      const values = ['lights_cycle'];
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
