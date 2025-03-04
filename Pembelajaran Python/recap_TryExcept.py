class InsufficientFundsError(Exception):
    """Exception khusus jika saldo tidak mencukupi"""
    def __init__(self, message="Saldo tidak mencukupi untuk transaksi ini"):
        super().__init__(message)


class InvalidTransactionError(Exception):
    """Exception khusus jika terjadi transaksi tidak valid"""
    def __init__(self, message="Transaksi tidak valid"):
        super().__init__(message)


def process_transaction(balance, amount):
    try:
        if amount <= 0:
            raise InvalidTransactionError("Jumlah transaksi harus lebih dari 0!")

        if amount > balance:
            raise InsufficientFundsError("Saldo tidak mencukupi!")

       
        if amount == 999:
            raise ValueError("Terjadi kesalahan sistem! Coba lagi.")

        new_balance = balance - amount
        print(f"Transaksi berhasil! Saldo tersisa: {new_balance}")
        return new_balance

    except InvalidTransactionError as e:
        print(f"Kesalahan Transaksi: {e}")
    except InsufficientFundsError as e:
        print(f"Kesalahan Saldo: {e}")
    except ValueError as e:
        print(f"Kesalahan Umum: {e}")
    except Exception as e:
        print(f"Kesalahan tak terduga: {e}")
    else:
        print("Transaksi selesai tanpa error.")
    finally:
        print("Transaksi selesai, terlepas dari sukses atau gagal.\n")



saldo_awal = 1000

try:
    saldo_awal = process_transaction(saldo_awal, 500)  
    saldo_awal = process_transaction(saldo_awal, -100)  
    saldo_awal = process_transaction(saldo_awal, 600)  
    saldo_awal = process_transaction(saldo_awal, 999)  
    saldo_awal = process_transaction(saldo_awal, "abc")  
except TypeError as e:
    print(f"Kesalahan Tipe Data: {e}")
except Exception as e:
    print(f"Kesalahan Umum di level utama: {e}")

print("Sistem transaksi selesai dijalankan.")
