export default {
  Query: {
    person: (parent: any, args: { id: string }): object => {
      const { id } = args;
      const result = { test: "Some value" };
      return result;
    },
    allPersons: (): any[] => []
  }
};
